# encoding:utf-8

# -----------------------------------
# Noise Anim Modifier
#
# Copyright (c) 2023 cignoir
# https://github.com/cignoir
# -----------------------------------

import random
import maya.cmds as cmds
from .easing import Easing


class AnimModifier:
    @classmethod
    def get_all_easing_types(cls):
        return Easing.all_types()

    def get_selected_attribute_keys(self, step, start_frame, end_frame, strength):
        selected_objects = cmds.ls(selection=True)

        selected_attributes = cmds.channelBox('mainChannelBox', query=True, selectedMainAttributes=True)
        if not selected_attributes:
            print("No attributes selected.")
            return None, None

        keys_info = {}

        for obj in selected_objects:
            for attr in selected_attributes:
                anim_curve = cmds.listConnections(obj + '.' + attr, type='animCurve')

                if anim_curve:
                    keys_info[obj + '.' + attr], keyframes = self.get_interpolated_values(obj + '.' + attr, start_frame,
                                                                                          end_frame, step)

        return keys_info, keyframes

    def get_interpolated_values(self, obj_attr, start_frame, end_frame, step):
        frames = [start_frame] + list(range(start_frame + step, end_frame, step)) + [end_frame]
        keyframes = cmds.keyframe(obj_attr, query=True)

        for keyframe in keyframes:
            if keyframe not in frames:
                frames.append(keyframe)

        frames.sort()
        values = [cmds.getAttr(obj_attr, time=f) for f in frames]
        return dict(zip(frames, values)), keyframes

    def get_easing_function(self, mode, ease_in, ease_out):
        return Easing.func(mode, ease_in, ease_out)

    def generate_random_values(self, keys_info, keyframes, strength, start_frame, end_frame, easing_function):
        random_values = {}
        for obj_attr in keys_info:
            random_values[obj_attr] = {}
            for frame in keys_info[obj_attr]:
                if frame not in keyframes:  # Only add random to non-keyframe frames
                    if start_frame < frame < end_frame:  # Only add random between the specified frames
                        x = (frame - start_frame) / (end_frame - start_frame)
                        prev = (frame - 1 - start_frame) / (end_frame - start_frame)
                        easing_value = easing_function(x) - easing_function(prev)
                        # print(f"{easing_value} = {easing_function(x)} - {easing_function(prev)}")
                        random_min = -strength * easing_value
                        random_max = strength * easing_value
                        random_values[obj_attr][frame] = random.uniform(random_min, random_max)
        return random_values

    def add_values_to_keys_info(self, keys_info, random_values):
        for obj_attr in keys_info:
            for frame in keys_info[obj_attr]:
                if frame in random_values[obj_attr]:
                    keys_info[obj_attr][frame] += random_values[obj_attr][frame]
        return keys_info

    def set_keys_from_info(self, keys_info, start_frame, end_frame):
        for obj_attr in keys_info:
            for frame, value in keys_info[obj_attr].items():
                if start_frame <= frame <= end_frame:  # Only set keyframes within the specified range
                    cmds.setKeyframe(obj_attr, time=frame, value=value)
