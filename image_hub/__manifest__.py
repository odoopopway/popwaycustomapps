
{
    "name": "Customer Image Workspace",
    "version": "1.0.0",
    "category": "Tools",
    "author": "Popway Software",
    "summary": "Customer-centric image gallery, comparison and timeline",
    "depends": ["base", "contacts"],
    "data": [
        "views/actions.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/image_views.xml",
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
    "installable": True
}
