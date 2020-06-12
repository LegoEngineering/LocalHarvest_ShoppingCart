#!/bin/bash

cd vue_apps/vue_app && npm install && npm run build && cd ../../docker_services && docker-compose up
