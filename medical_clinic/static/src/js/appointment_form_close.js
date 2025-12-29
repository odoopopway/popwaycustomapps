/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

patch(FormController.prototype, {

    async onSaveError(error) {
        let result;

        try {
            result = await super.onSaveError(error);
        } catch (e) {
            // Odoo sometimes throws instead of returning
            result = null;
        }

        // 🔥 ALWAYS return discard object
        return result ?? { discard: false };
    },

});
