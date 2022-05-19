#!/bin/bash

export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
rq worker queue_1 default --with-scheduler
