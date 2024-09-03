FROM ros:noetic

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-noetic-rospy \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /ros_workspace/src
WORKDIR /ros_workspace

COPY ./ros_package /ros_workspace/src/ros_package

