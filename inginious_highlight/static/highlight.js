"use strict";

const CLASSES_TO_REMOVE = ["ph-default", "ph-blue", "ph-darkblue", "ph-red",
    "ph-darkred", "ph-green", "ph-darkgreen", "ph-yellow", "ph-orange"].join(' ');

function clear_highlight() {
    jQuery(".CodeMirror-linebackground").removeClass(CLASSES_TO_REMOVE);
}