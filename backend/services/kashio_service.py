import requests

def ejecutar_credito(data):
    payload = {
        "external_id": "0000001",
        "channel": "WEB",
        "method": "CASH",
        "psp_account": {"public_id": data["account_id"]},
        "total": {
            "currency": data["currency"],
            "value": float(data["amount"])
        },
        "is_confirmed": True,
        "metadata": {
            "description": data["description"]
        }
    }

    r = requests.post(
        data["url"],
        json=payload,
        auth=(data["user"], data["password"])
    )

    return {
        "status": r.status_code,
        "response": r.json() if r.text else {}
    }


def ejecutar_debito(data):
    payload = {
        "total": {
            "currency": data["currency"],
            "value": float(data["amount"])
        },
        "account": {
            "public_id": data["account_id"]
        },
        "psp_operation_id": "AUTO123",
        "psp_operation_date": data["date"],
        "metadata": {
            "description": data["description"]
        }
    }

    r = requests.post(
        data["url"],
        json=payload,
        auth=(data["user"], data["password"])
    )

    return {
        "status": r.status_code,
        "response": r.json() if r.text else {}
    }
