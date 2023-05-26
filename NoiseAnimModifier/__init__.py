# encoding:utf-8

# -----------------------------------
# Noise Anim Modifier
#
# Copyright (c) 2023 cignoir
# https://github.com/cignoir
# MIT License
# -----------------------------------

from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

import maya.cmds as cmds

from .anim_modifier import AnimModifier


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class MainDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(MainDialog, self).__init__(parent)
        self.setWindowTitle("NoiseAnimModifier")
        self.setMinimumWidth(200)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.modifier_combobox = QtWidgets.QComboBox()
        self.modifier_combobox.addItems(["Random"])

        self.easing_combobox = QtWidgets.QComboBox()
        self.easing_combobox.addItems(AnimModifier.get_all_easing_types())
        self.easing_checkbox_in = QtWidgets.QCheckBox("In")
        self.easing_checkbox_out = QtWidgets.QCheckBox("Out")

        self.strength_spinbox = QtWidgets.QDoubleSpinBox()
        self.strength_spinbox.setRange(0, 100000)
        self.strength_spinbox.setDecimals(1)
        self.strength_spinbox.setValue(100.0)

        self.frame_start_spinbox = QtWidgets.QSpinBox()
        self.frame_start_spinbox.setRange(0, 100000)
        self.frame_start_spinbox.setValue(1)
        self.frame_end_spinbox = QtWidgets.QSpinBox()
        self.frame_end_spinbox.setRange(0, 100000)
        self.frame_end_spinbox.setValue(120)

        self.step_spinbox = QtWidgets.QSpinBox()
        self.step_spinbox.setRange(0, 100000)
        self.step_spinbox.setValue(2)

        self.motion_trail_checkbox = QtWidgets.QCheckBox("Create motion trail")
        self.motion_trail_checkbox.setChecked(True)

        self.apply_button = QtWidgets.QPushButton("Apply")
        self.undo_button = QtWidgets.QPushButton("Undo")
        self.cancel_button = QtWidgets.QPushButton("Cancel")

    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        range_layout = QtWidgets.QHBoxLayout()
        range_layout.addWidget(self.frame_start_spinbox)
        range_layout.addWidget(QtWidgets.QLabel(" - "))
        range_layout.addWidget(self.frame_end_spinbox)

        easing_layout = QtWidgets.QHBoxLayout()
        easing_layout.addWidget(self.easing_combobox)
        easing_layout.addWidget(self.easing_checkbox_in)
        easing_layout.addWidget(self.easing_checkbox_out)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("Modifier:", self.modifier_combobox)
        form_layout.addRow("Easing:", easing_layout)
        form_layout.addRow("Range:", range_layout)
        form_layout.addRow("Strength:", self.strength_spinbox)
        form_layout.addRow("Step:", self.step_spinbox)
        main_layout.addLayout(form_layout)

        main_layout.addWidget(self.motion_trail_checkbox)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.undo_button)
        button_layout.addWidget(self.cancel_button)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.apply_button.clicked.connect(self.on_apply_button_clicked)
        self.undo_button.clicked.connect(self.on_undo_button_clicked)
        self.cancel_button.clicked.connect(self.close)

    def on_apply_button_clicked(self):
        selected = cmds.ls(sl=True)
        selected_attributes = cmds.channelBox('mainChannelBox', query=True, selectedMainAttributes=True)
        if not selected_attributes:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("No attributes selected.")
            msgBox.exec()
            return

        cmds.undoInfo(openChunk=True)

        start_frame = self.frame_start_spinbox.value()
        end_frame = self.frame_end_spinbox.value()
        strength = self.strength_spinbox.value()
        step = self.step_spinbox.value()

        easing_mode = self.easing_combobox.currentText()
        is_ease_in = self.easing_checkbox_in.isChecked()
        is_ease_out = self.easing_checkbox_out.isChecked()
        is_motion_trail = self.motion_trail_checkbox.isChecked()

        modifier = AnimModifier()

        keys_info, keyframes = modifier.get_selected_attribute_keys(step, start_frame, end_frame, strength)
        easing_func = modifier.get_easing_function(easing_mode, is_ease_in, is_ease_out)
        random_values = modifier.generate_random_values(keys_info, keyframes, strength, start_frame, end_frame,
                                                        easing_func)
        keys_info = modifier.add_values_to_keys_info(keys_info, random_values)
        modifier.set_keys_from_info(keys_info, start_frame, end_frame)

        cmds.select(selected)

        if is_motion_trail:
            start_time = cmds.playbackOptions(q=True, min=True)
            end_time = cmds.playbackOptions(q=True, max=True)
            cmds.snapshot(motionTrail=True, increment=True, startTime=start_time, endTime=end_time)

        cmds.undoInfo(closeChunk=True)

    def on_undo_button_clicked(self):
        cmds.undo()

if __name__ == "__main__":
    try:
        main_dialog.close()
        main_dialog.deleteLater()
    except:
        pass
    main_dialog = MainDialog()
    main_dialog.show()
