/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { CalendarController } from "@web/views/calendar/calendar_controller";

patch(CalendarController.prototype, {

    getCalendarOptions() {
        const options = super.getCalendarOptions();

        // ⏰ Clinic working hours
        options.slotMinTime = "09:00:00";
        options.slotMaxTime = "18:00:00";

        // ⏱ TRUE 30-minute grid
        options.slotDuration = "00:30:00";

        // 🔒 Force click & drag snapping (NO 9:15 / 9:45)
        options.snapDuration = "00:30:00";

        // 🕘 Show labels at 9, 9:30, 10, 10:30
        options.slotLabelInterval = "00:30:00";
        options.slotLabelFormat = {
            hour: "numeric",
            minute: "2-digit",
            omitZeroMinute: false,
            meridiem: "short",
        };

        // 🧭 Auto scroll to clinic start
        options.scrollTime = "09:00:00";

        // ❌ Never show time inside events
        options.displayEventTime = false;

        // 📦 Block-style events
        options.eventDisplay = "block";

        // 🧾 ONLY display_name (patient | mobile)
        options.eventContent = function (arg) {
            return {
                html: `
                    <div class="clinic-event">
                        <strong>${arg.event.title}</strong>
                    </div>
                `
            };
        };

        return options;
    }

});
