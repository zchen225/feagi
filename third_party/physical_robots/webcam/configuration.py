#!/usr/bin/env python3
"""
Copyright 2016-2022 The FEAGI Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import os


feagi_settings = {
    # "feagi_auth_url": "http://127.0.0.1:9000/v1/k8/feagi_settings/auth_token",
    "feagi_url": None,
    "feagi_dns": None,
    "feagi_host": os.environ.get('FEAGI_HOST_INTERNAL', "127.0.0.1"),
    "feagi_api_port": os.environ.get('FEAGI_API_PORT', "8000")
}
agent_settings = {
    "agent_data_port": "10006",
    "agent_id": "javascript_webcam",
    "agent_type": "embodiment",
    'TTL': 2,
    'last_message': 0,
    'godot_websocket_ip': "0.0.0.0",
    'godot_websocket_port': os.environ.get('WS_WEBCAM_PORT', "9051")
}

capabilities = {
    "camera": {
        "type": "ipu",
        "disabled": False,
        "count": 1,
        "width": 128,
        "height": 128,
        "deviation_threshold": 0.4,
        "retina_width_percent": 95,
        "retina_height_percent": 80,
        "central_vision_compression": [64, 64],
        "peripheral_vision_compression": [8, 8],
        "previous_data": {},
        "video_device_index": 2,
        "aperture_range": [0.1, 2],
        "aperture_default": 2
    }
}

message_to_feagi = {"data": {}}

