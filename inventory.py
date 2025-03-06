from fastapi import APIRouter
import json

router = APIRouter()

inventories = '''[
{
    "params": {
        "fields": "variant_options,variant_types,vendors,tags,brands",
        "extras": "channels,log,product_listings",
        "store_id": 1374789,
        "product_id": "13322526",
        "channel_availability": [
            "storefront",
            "pos",
            "shopping_app"
        ]
    },
    "data": {
        "product": {
            "id": 13322526,
            "store_id": 1374789,
            "reference_id": null,
            "universal_category_id": 500035,
            "title": "Wekome WDC-47 Magnetic Data Cable 65W 1M(PD 35W)",
            "name": "Wekome WDC-47 Magnetic Data Cable 65W 1M(PD 35W)",
            "meta_title": "Wekome WDC-47 Magnetic Data Cable 65W 1M(PD 35W)",
            "description": "Wekome Magnetic Data Cable 66W: a cutting-edge, tangle-free solution for your charging and data transfer needs. Featuring an innovative magnetic design, this cable automatically rolls up for easy storage, eliminating clutter. The adjustable length en",
            "taxable": false,
            "shipping_required": true,
            "position": 8,
            "handle": "wekome-wdc-47-magnetic-data-cable-65w-1m-pd-35w-",
            "min_price": "12.9",
            "max_price": "12.9",
            "inventory_management": "easystore",
            "total_quantity": 100,
            "keywords": null,
            "body_html": "\u003cp\u003eWekome Magnetic Data Cable 66W: a cutting-edge, tangle-free solution for your charging and data transfer needs. Featuring an innovative magnetic design, this cable automatically rolls up for easy storage, eliminating clutter. The adjustable length ensures maximum convenience, while the 500N super strong magnetism keeps the cable securely in place. With a high-power output of 66W/65W/PD35W and 480mbps data transmission, this 1000mm cable delivers exceptional performance for all your devices\u003c/p\u003e",
            "origin_body_html": null,
            "note": null,
            "discounts": null,
            "stock_qty_mark": true,
            "bundle_json": null,
            "view_count": 0,
            "unique_view_count": 0,
            "recommended_product_ids": null,
            "recommended_at": null,
            "is_deleted": false,
            "deleted_at": null,
            "published_at": "2025-02-10T16:18:00.000+08:00",
            "updated_at": "2025-02-27T17:11:47.000+08:00",
            "created_at": "2025-02-10T16:18:45.000+08:00",
            "admin_links": [],
            "is_published": true,
            "visibility": "published",
            "image_url": "https://cdn.store-assets.com/s/1374789/i/83081961.jpg",
            "variants": [
                {
                    "id": 61761598,
                    "product_id": 13322526,
                    "image_id": 0,
                    "options": null,
                    "name": null,
                    "sku": "6941027650202",
                    "barcode": null,
                    "width": "7.0",
                    "height": "3.0",
                    "length": "2.0",
                    "weight": "0.3",
                    "weight_unit": "kg",
                    "grams": "300.0",
                    "price": "12.9",
                    "compare_at_price": "0.0",
                    "cost_price": "0.0",
                    "inventory_quantity": 100,
                    "inventory_policy": false,
                    "taxable": false,
                    "shipping_required": true,
                    "components_required": false,
                    "position": 1,
                    "discounts": null,
                    "is_enabled": true,
                    "is_deleted": false,
                    "deleted_at": null,
                    "updated_at": "2025-02-27T17:11:47.000+08:00",
                    "created_at": "2025-02-10T16:18:45.000+08:00",
                    "image_url": null,
                    "purchasable": true,
                    "inventory_management": "easystore",
                    "inventory_levels": [
                        {
                            "variant_id": 61761598,
                            "location_id": 1278142,
                            "inventory_quantity": 100,
                            "incoming_inventory_quantity": 0,
                            "shelf": null,
                            "last_adjusted_at": null,
                            "updated_at": "2025-02-27T17:11:47.000+08:00"
                        }
                    ],
                    "shipping_profile": {
                        "id": 534725,
                        "store_id": 1374789,
                        "name": "Default Profile",
                        "condition": "general",
                        "is_enabled": true,
                        "is_deleted": false,
                        "deleted_at": null,
                        "updated_at": "2025-02-10T10:58:53.000+08:00",
                        "created_at": "2025-02-10T10:58:53.000+08:00",
                        "is_default": true
                    },
                    "shelf": null,
                    "variant_options": []
                }
            ],
            "variant_options": [],
            "variant_types": [],
            "variant_ids": [
                61761598
            ],
            "collections": [
                {
                    "id": 4362583,
                    "store_id": 1374789,
                    "parent_id": 4362582,
                    "reference_id": null,
                    "name": "Cables",
                    "title": "Cables",
                    "handle": "cables",
                    "image_url": "https://cdn.store-assets.com/s/1374789/f/14765561.png",
                    "origin_image_url": null,
                    "description": "",
                    "body_html": "",
                    "origin_body_html": null,
                    "position": 9,
                    "is_locked": false,
                    "is_published": true,
                    "published_at": "2025-02-26T14:21:59.000+08:00",
                    "updated_at": "2025-02-26T14:22:00.000+08:00",
                    "created_at": "2025-02-10T14:08:57.000+08:00"
                }
            ],
            "images": [
                {
                    "id": 83081961,
                    "store_id": 1374789,
                    "product_id": 13322526,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 1,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83081961.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83081961.jpg",
                    "size": 66179,
                    "height": 1024,
                    "width": 1024,
                    "title": "f7e62e6750504d5ea646eda0f31fa856~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:18:45.000+08:00"
                },
                {
                    "id": 83081962,
                    "store_id": 1374789,
                    "product_id": 13322526,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 2,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83081962.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83081962.jpg",
                    "size": 54496,
                    "height": 1024,
                    "width": 1024,
                    "title": "4f86fe227443462ba68585d25af20e92~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:18:46.000+08:00"
                },
                {
                    "id": 83081963,
                    "store_id": 1374789,
                    "product_id": 13322526,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 3,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83081963.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83081963.jpg",
                    "size": 73402,
                    "height": 1024,
                    "width": 1024,
                    "title": "c5bfe940a4ac4d16b70c04d67708fd3d~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:18:46.000+08:00"
                }
            ],
            "inventory_levels": [
                {
                    "variant_id": 61761598,
                    "location_id": 1278142,
                    "inventory_quantity": 100,
                    "incoming_inventory_quantity": 0,
                    "shelf": null,
                    "last_adjusted_at": null,
                    "updated_at": "2025-02-27T17:11:47.000+08:00"
                }
            ],
            "total_incoming_inventory_quantity": 0,
            "vendors": [],
            "tags": [],
            "brands": [],
            "shortlink_hash": "1xh9pok05",
            "is_bundle": false,
            "product_bundle": null,
            "last_updated_at": "2025-02-27T17:11:47.000+08:00",
            "limit_count": 39,
            "channels": [
                {
                    "is_available": true,
                    "is_enabled": true,
                    "kind": "storefront",
                    "route": "/channels/storefront",
                    "is_published": true,
                    "published_at": null
                }
            ],
            "google_shopping": {
                "name": "Google Shopping",
                "icon": "/images/icons/channels/google_shopping.png",
                "is_google_product": false
            },
            "facebook_catalog": {
                "name": "Facebook Catalog",
                "icon": "/images/facebook/facebook_catalog.png",
                "featured_in_fb_catalog": false,
                "is_catalog_connected": false
            },
            "instagram": {
                "name": "Instagram",
                "icon": "/images/icons/channels/instagram.png",
                "featured_in_instagram": false
            }
        },
        "vendors": [],
        "tags": [
            {
                "id": 714989,
                "name": "charger"
            },
            {
                "id": 714990,
                "name": "car charger"
            }
        ],
        "brands": [
            {
                "id": 277066,
                "name": "Wekome"
            }
        ],
        "prev_next": {
            "prev_id": 13322527,
            "next_id": 13322525,
            "params": {
                "fields": "variant_options,variant_types,vendors,tags,brands",
                "extras": "channels,log,product_listings",
                "store_id": 1374789,
                "product_id": "13322526",
                "channel_availability": [
                    "storefront",
                    "pos",
                    "shopping_app"
                ]
            }
        }
    }
}
]'''

inventories = json.loads(inventories)

@router.get("/api/inventories")
async def get_inventories():
    return inventories

