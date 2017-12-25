[
    {
        "id": "8c483034.02fff",
        "type": "tab",
        "label": "Flow 3"
    },
    {
        "id": "9a6687cc.f9b81",
        "type": "rpi-gpio in",
        "z": "8c483034.02fff",
        "name": "button",
        "pin": "7",
        "intype": "tri",
        "debounce": "25",
        "read": true,
        "x": 205,
        "y": 156.9499969482422,
        "wires": [
            [
                "4daf97f5.c5fce4",
                "7efddf21.e0bbac"
            ]
        ]
    },
    {
        "id": "4daf97f5.c5fce4",
        "type": "switch",
        "z": "8c483034.02fff",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 370,
        "y": 160,
        "wires": [
            [
                "c6bf17c.b9f2ca8"
            ],
            [
                "e58a6f0f.53bcf"
            ]
        ]
    },
    {
        "id": "c6bf17c.b9f2ca8",
        "type": "change",
        "z": "8c483034.02fff",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 550,
        "y": 100,
        "wires": [
            [
                "a962ef77.c6c738"
            ]
        ]
    },
    {
        "id": "e58a6f0f.53bcf",
        "type": "change",
        "z": "8c483034.02fff",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 550,
        "y": 180,
        "wires": [
            [
                "a962ef77.c6c738"
            ]
        ]
    },
    {
        "id": "7efddf21.e0bbac",
        "type": "debug",
        "z": "8c483034.02fff",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 314,
        "y": 317.94000244140625,
        "wires": []
    },
    {
        "id": "a962ef77.c6c738",
        "type": "rpi-gpio out",
        "z": "8c483034.02fff",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 710,
        "y": 140,
        "wires": []
    }
]
