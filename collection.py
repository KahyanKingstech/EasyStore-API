from fastapi import FastAPI, APIRouter
import json

app = FastAPI()

router = APIRouter()

collections = '''[
{
    "permitted": {
        "store_id": 1374789,
        "collection_id": "4362583"
    },
    "data": {
        "id": 4362583,
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
        "created_at": "2025-02-10T14:08:57.000+08:00",
        "visibility": "published",
        "products": [
            "WEKOME WDC-32 Fast Charge, 1 Meter Cable (Black) Alloy Aluminum Alloy Aluminum",
            "Wekome WDC-47 Magnetic Data Cable 65W 1M(PD 35W)"
        ]
    }
},
{
    "permitted": {
        "store_id": 1374789,
        "collection_id": "4362592"
    },
    "data": {
        "id": 4362592,
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
        "created_at": "2025-02-10T14:10:12.000+08:00",
        "visibility": "published",
        "products": [
            "WEKOME WP-19 Fast Charging Mini 3-in-1 5000mAh Power Bank",
            "WEKOME WP-77 Ultra-thin Magnetic Wireless Power Bank 5000mAh Fast Charge 15W"
        ]
    }
},
{
    "permitted": {
        "store_id": 1374789,
        "collection_id": "4362580"
    },
    "data": {
        "id": 4362580,
        "name": "Car Charger",
        "title": "Car Charger",
        "handle": "car-charger",
        "image_url": "https://cdn.store-assets.com/s/1374789/f/14765724.jpg",
        "origin_image_url": null,
        "description": "",
        "body_html": "",
        "origin_body_html": null,
        "position": 7,
        "is_locked": false,
        "is_published": true,
        "published_at": "2025-02-26T14:21:50.000+08:00",
        "updated_at": "2025-02-26T14:21:50.000+08:00",
        "created_at": "2025-02-10T14:06:09.000+08:00",
        "visibility": "published",
        "products": [
            "WEKOME WP-C45 Car Charger (A+C) 43W – Fast Charging for Your Phone"
        ]
    }
}
]'''

collections = json.loads(collections)

@router.get("/api/collections")
async def get_collections():
    return collections
