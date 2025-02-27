from fastapi import APIRouter
import json

router = APIRouter()

products = '''[
{
    "params": {
        "store_id": 1374789,
        "product_id": "13322534",
        "channel_availability": [
            "storefront",
            "pos",
            "shopping_app"
        ]
    },
    "data": {
        "product": {
            "id": 13322534,
            "store_id": 1374789,
            "reference_id": null,
            "universal_category_id": 6292,
            "title": "WEKOME WP-19 Fast Charging Mini 3-in-1 5000mAh Power Bank",
            "name": "WEKOME WP-19 Fast Charging Mini 3-in-1 5000mAh Power Bank",
            "meta_title": "WEKOME WP-19 Fast Charging Mini 3-in-1 5000mAh Power Bank",
            "description": "Experience Power on the Go with the Ultra-Compact 22.5W Power BankPerfect for travel, work, or daily use, this power bank is your ultimate companion for uninterrupted power wherever life takes you.",
            "taxable": false,
            "shipping_required": true,
            "position": 13,
            "handle": "wekome-wp-19-fast-charging-mini-3-in-1-5000mah-power-bank",
            "min_price": "29.0",
            "max_price": "29.0",
            "inventory_management": "easystore",
            "total_quantity": 299,
            "keywords": null,
            "body_html": "\u003cp\u003eExperience Power on the Go with the Ultra-Compact 22.5W Power Bank\u003c/p\u003e\u003cp\u003ePerfect for travel, work, or daily use, this power bank is your ultimate companion for uninterrupted power wherever life takes you.\u003c/p\u003e",
            "origin_body_html": null,
            "note": null,
            "discounts": null,
            "stock_qty_mark": true,
            "bundle_json": null,
            "view_count": 0,
            "unique_view_count": 0,
            "recommended_product_ids": "13322532,13318347,13321861,13322531,13321841,13322530,13322525,13322527,13322526,13322523",
            "recommended_at": "2025-02-12T15:05:21.000+08:00",
            "is_deleted": false,
            "deleted_at": null,
            "published_at": "2025-02-10T16:19:00.000+08:00",
            "updated_at": "2025-02-26T15:11:57.000+08:00",
            "created_at": "2025-02-10T16:19:22.000+08:00",
            "admin_links": [],
            "is_published": true,
            "visibility": "published",
            "image_url": "https://cdn.store-assets.com/s/1374789/i/83082035.jpg",
            "variants": [
                {
                    "id": 61761716,
                    "product_id": 13322534,
                    "image_id": 83082035,
                    "options": "#10379889_36222352e",
                    "name": "Beige",
                    "sku": "6941027649435",
                    "barcode": null,
                    "width": "7.0",
                    "height": "3.0",
                    "length": "2.0",
                    "weight": "0.5",
                    "weight_unit": "kg",
                    "grams": "500.0",
                    "price": "29.0",
                    "compare_at_price": "0.0",
                    "cost_price": "0.0",
                    "inventory_quantity": 99,
                    "inventory_policy": false,
                    "taxable": false,
                    "shipping_required": true,
                    "components_required": false,
                    "position": 1,
                    "discounts": null,
                    "is_enabled": true,
                    "is_deleted": false,
                    "deleted_at": null,
                    "updated_at": "2025-02-26T16:29:55.000+08:00",
                    "created_at": "2025-02-10T16:19:22.000+08:00",
                    "image_url": "https://cdn.store-assets.com/s/1374789/i/83082035.jpg",
                    "purchasable": true,
                    "inventory_management": "easystore",
                    "inventory_levels": [
                        {
                            "variant_id": 61761716,
                            "location_id": 1278142,
                            "inventory_quantity": 99,
                            "incoming_inventory_quantity": 0,
                            "shelf": null,
                            "last_adjusted_at": null,
                            "updated_at": "2025-02-26T15:10:24.000+08:00"
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
                    "variant_options": [
                        {
                            "id": 36222352,
                            "variant_type_id": 10379889,
                            "name": "Beige"
                        }
                    ]
                },
                {
                    "id": 61761719,
                    "product_id": 13322534,
                    "image_id": 83082040,
                    "options": "#10379889_36222353e",
                    "name": "Black",
                    "sku": "6941027649459",
                    "barcode": null,
                    "width": "7.0",
                    "height": "3.0",
                    "length": "2.0",
                    "weight": "0.5",
                    "weight_unit": "kg",
                    "grams": "500.0",
                    "price": "29.0",
                    "compare_at_price": "0.0",
                    "cost_price": "0.0",
                    "inventory_quantity": 100,
                    "inventory_policy": false,
                    "taxable": false,
                    "shipping_required": true,
                    "components_required": false,
                    "position": 2,
                    "discounts": null,
                    "is_enabled": true,
                    "is_deleted": false,
                    "deleted_at": null,
                    "updated_at": "2025-02-26T16:29:55.000+08:00",
                    "created_at": "2025-02-10T16:19:22.000+08:00",
                    "image_url": "https://cdn.store-assets.com/s/1374789/i/83082040.jpg",
                    "purchasable": true,
                    "inventory_management": "easystore",
                    "inventory_levels": [
                        {
                            "variant_id": 61761719,
                            "location_id": 1278142,
                            "inventory_quantity": 100,
                            "incoming_inventory_quantity": 0,
                            "shelf": null,
                            "last_adjusted_at": null,
                            "updated_at": "2025-02-10T16:19:22.000+08:00"
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
                    "variant_options": [
                        {
                            "id": 36222353,
                            "variant_type_id": 10379889,
                            "name": "Black"
                        }
                    ]
                },
                {
                    "id": 61761721,
                    "product_id": 13322534,
                    "image_id": 83082037,
                    "options": "#10379889_36222354e",
                    "name": "Green",
                    "sku": "6941027649442",
                    "barcode": null,
                    "width": "7.0",
                    "height": "3.0",
                    "length": "2.0",
                    "weight": "0.5",
                    "weight_unit": "kg",
                    "grams": "500.0",
                    "price": "29.0",
                    "compare_at_price": "0.0",
                    "cost_price": "0.0",
                    "inventory_quantity": 100,
                    "inventory_policy": false,
                    "taxable": false,
                    "shipping_required": true,
                    "components_required": false,
                    "position": 3,
                    "discounts": null,
                    "is_enabled": true,
                    "is_deleted": false,
                    "deleted_at": null,
                    "updated_at": "2025-02-26T16:29:55.000+08:00",
                    "created_at": "2025-02-10T16:19:22.000+08:00",
                    "image_url": "https://cdn.store-assets.com/s/1374789/i/83082037.jpg",
                    "purchasable": true,
                    "inventory_management": "easystore",
                    "inventory_levels": [
                        {
                            "variant_id": 61761721,
                            "location_id": 1278142,
                            "inventory_quantity": 100,
                            "incoming_inventory_quantity": 0,
                            "shelf": null,
                            "last_adjusted_at": null,
                            "updated_at": "2025-02-10T16:19:22.000+08:00"
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
                    "variant_options": [
                        {
                            "id": 36222354,
                            "variant_type_id": 10379889,
                            "name": "Green"
                        }
                    ]
                }
            ],
            "variant_options": [
                {
                    "id": 36222352,
                    "variant_type_id": 10379889,
                    "name": "Beige",
                    "position": 1,
                    "is_deleted": false,
                    "created_at": "2025-02-10T16:19:22.000+08:00"
                },
                {
                    "id": 36222353,
                    "variant_type_id": 10379889,
                    "name": "Black",
                    "position": 2,
                    "is_deleted": false,
                    "created_at": "2025-02-10T16:19:22.000+08:00"
                },
                {
                    "id": 36222354,
                    "variant_type_id": 10379889,
                    "name": "Green",
                    "position": 3,
                    "is_deleted": false,
                    "created_at": "2025-02-10T16:19:22.000+08:00"
                }
            ],
            "variant_types": [
                {
                    "id": 10379889,
                    "product_id": 13322534,
                    "name": "Color",
                    "position": 1,
                    "is_deleted": false,
                    "created_at": "2025-02-10T16:19:22.000+08:00"
                }
            ],
            "variant_ids": [
                61761716,
                61761719,
                61761721
            ],
            "collections": [
                {
                    "id": 4362592,
                    "store_id": 1374789,
                    "parent_id": 4362589,
                    "reference_id": null,
                    "name": "5000mAh",
                    "title": "5000mAh",
                    "handle": "5000mah",
                    "image_url": "https://cdn.store-assets.com/s/1374789/f/14765558.png",
                    "origin_image_url": null,
                    "description": "",
                    "body_html": "",
                    "origin_body_html": null,
                    "position": 17,
                    "is_locked": false,
                    "is_published": true,
                    "published_at": "2025-02-26T15:02:30.000+08:00",
                    "updated_at": "2025-02-26T15:02:30.000+08:00",
                    "created_at": "2025-02-10T14:10:12.000+08:00"
                }
            ],
            "images": [
                {
                    "id": 83082035,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 1,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082035.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082035.jpg",
                    "size": 54955,
                    "height": 1000,
                    "width": 1000,
                    "title": "8f7973a57b734c0e88a21076f358465f~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:22.000+08:00"
                },
                {
                    "id": 83082036,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 2,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082036.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082036.jpg",
                    "size": 120548,
                    "height": 1000,
                    "width": 1000,
                    "title": "70e61654ffcd43f58222a28d7b825e5b~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:23.000+08:00"
                },
                {
                    "id": 83082037,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 3,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082037.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082037.jpg",
                    "size": 61454,
                    "height": 1000,
                    "width": 1000,
                    "title": "4e0818496c554dcf9c138706c4d3b9d4~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:23.000+08:00"
                },
                {
                    "id": 83082038,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 4,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082038.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082038.jpg",
                    "size": 81399,
                    "height": 1000,
                    "width": 1000,
                    "title": "90a0445c429947e8b2e8bc7581e821eb~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:23.000+08:00"
                },
                {
                    "id": 83082039,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 5,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082039.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082039.jpg",
                    "size": 104998,
                    "height": 1000,
                    "width": 1000,
                    "title": "5831c7bb6ef742edb2ed2478c8b61854~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:23.000+08:00"
                },
                {
                    "id": 83082040,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 6,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082040.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082040.jpg",
                    "size": 90688,
                    "height": 1000,
                    "width": 1000,
                    "title": "bf4fe59daed34ff091dd1927ddba2925~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:24.000+08:00"
                },
                {
                    "id": 83082041,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 7,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082041.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082041.jpg",
                    "size": 103928,
                    "height": 1000,
                    "width": 1000,
                    "title": "f7c2914e7ae84663b1752da99d0927d9~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:24.000+08:00"
                },
                {
                    "id": 83082042,
                    "store_id": 1374789,
                    "product_id": 13322534,
                    "format_type": "Images",
                    "youtube_id": null,
                    "position": 8,
                    "extension": "jpg",
                    "url": "https://cdn.store-assets.com/s/1374789/i/83082042.jpg",
                    "origin_url": "https://s3.ap-southeast-1.amazonaws.com/cdn.store-assets.com/s/1374789/i/83082042.jpg",
                    "size": 109774,
                    "height": 1000,
                    "width": 1000,
                    "title": "8bbab8eea5024ca0855f3b22d5214c89~tplv-o3syd03w52-origin-jpeg",
                    "is_deleted": false,
                    "deleted_at": null,
                    "s3_deleted": false,
                    "s3_deleted_at": null,
                    "created_at": "2025-02-10T16:19:24.000+08:00"
                }
            ],
            "inventory_levels": [
                {
                    "variant_id": 61761716,
                    "location_id": 1278142,
                    "inventory_quantity": 99,
                    "incoming_inventory_quantity": 0,
                    "shelf": null,
                    "last_adjusted_at": null,
                    "updated_at": "2025-02-26T15:10:24.000+08:00"
                }
            ],
            "total_incoming_inventory_quantity": 0,
            "vendors": [],
            "tags": [],
            "brands": [],
            "shortlink_hash": "g3hogrjxz",
            "is_bundle": false,
            "product_bundle": null,
            "last_updated_at": "2025-02-26T16:29:55.000+08:00",
            "limit_count": 39
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
            "prev_id": null,
            "next_id": 13322532,
            "params": {
                "store_id": 1374789,
                "product_id": "13322534",
                "channel_availability": [
                    "storefront",
                    "pos",
                    "shopping_app"
                ]
            }
        }
    }
},
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
            "total_quantity": 248,
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
            "updated_at": "2025-02-26T15:10:55.000+08:00",
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
                    "inventory_quantity": 248,
                    "inventory_policy": false,
                    "taxable": false,
                    "shipping_required": true,
                    "components_required": false,
                    "position": 1,
                    "discounts": null,
                    "is_enabled": true,
                    "is_deleted": false,
                    "deleted_at": null,
                    "updated_at": "2025-02-26T15:10:55.000+08:00",
                    "created_at": "2025-02-10T16:18:45.000+08:00",
                    "image_url": null,
                    "purchasable": true,
                    "inventory_management": "easystore",
                    "inventory_levels": [
                        {
                            "variant_id": 61761598,
                            "location_id": 1278142,
                            "inventory_quantity": 248,
                            "incoming_inventory_quantity": 0,
                            "shelf": null,
                            "last_adjusted_at": null,
                            "updated_at": "2025-02-26T15:10:55.000+08:00"
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
                    "inventory_quantity": 248,
                    "incoming_inventory_quantity": 0,
                    "shelf": null,
                    "last_adjusted_at": null,
                    "updated_at": "2025-02-26T15:10:55.000+08:00"
                }
            ],
            "total_incoming_inventory_quantity": 0,
            "vendors": [],
            "tags": [],
            "brands": [],
            "shortlink_hash": "1xh9pok05",
            "is_bundle": false,
            "product_bundle": null,
            "last_updated_at": "2025-02-26T15:10:55.000+08:00",
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

products = json.loads(products)

@router.get("/api/products")
async def get_products():
    return products

