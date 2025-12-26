{
    "name": "Customer Image Workspace",
    "version": "1.0.0",
    "category": "Tools",
    "summary": """<p>This module provides a <strong>customer-centric image gallery</strong> that allows you to manage, compare, and view customer images in a timeline. Features include:</p>
                  <ul>
                    <li>Image gallery with zoom and editing features.</li>
                    <li>Customer image comparison tools.</li>
                    <li>Timeline view to track image updates.</li>
                  </ul>""",  # HTML format description
    "author": "Popway Software",
    "depends": ["base", "contacts"],
    "data": [
        "views/category_views.xml",
        "views/customer_image_kanban_view.xml",
        "views/tag_views.xml",
        "views/customer_image_tree.xml",
        "views/workspace_views.xml",
        "views/comparison_views.xml",
        "views/menu.xml",
        'wizard/customer_image_upload_wizard.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "image_hub/static/src/css/image_zoom.css",
            'image_hub/static/src/js/image_editor.js',
            'image_hub/static/src/xml/image_editor.xml',
            'https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.0/fabric.min.js',
        ],
    },
    "application": True,
    "installable": True,
    "website": "https://www.popwaysoftware.com",
    "icon": "/image_hub/static/description/icon.png",  # Path to your icon image
    "cover_image": "/image_hub/static/description/cover_image.jpg",  # Path to the cover image (JPG)
    "license": "AGPL-3",  # License you are using (AGPL-3 in this case)
}
