odoo.define("estate.color_piller", function (require) {
  "use strict";

  var AbstractField = require("web.AbstractField");
  var fieldRegistry = require("web.field_registry");
  var rpc = require("web.rpc");

  var colorField = AbstractField.extend({
    className: "o_int_color",
    tagName: "span",
    supportedFieldTypes: ["integer"],

    events: {
      "click .o_color_pill": "clickColorPill",
    },

    init: function () {
      this.totalColors = 10;
      this.colorCount = 0;
      this._super.apply(this, arguments);
    },

    start: function () {
      this._super.apply(this, arguments);
      // Fetch the total count of records with a non-empty color field
      if (this.mode === "edit") {
        this._fetchColorCount();
      }
    },

    _fetchColorCount: function () {
      // Make an RPC call to get the count of records with the selected color
      var self = this;
      rpc
        .query({
          model: "demo.widget", // Replace with your actual model name
          method: "search_count",
          args: [[["color", ">", 0]]], // Query records with the selected color
        })
        .then(function (count) {
          self.colorCount = count;
          self._renderColorCount(); // Update the display of colorCount
        });
    },

    _renderColorCount: function () {
      // Display the color count below the color pills
      if (this.$el.find(".color_count").length === 0) {
        this.$el.append(
          $("<div>", {
            class: "color_count",
            text: "colorCount " + this.colorCount,
          })
        );
      } else {
        this.$el.find(".color_count").text("colorCount " + this.colorCount);
      }
    },

    _renderEdit: function () {
      this.$el.empty();
      for (let i = 1; i <= this.totalColors; i++) {
        var className = "o_color_pill o_color_" + i;
        if (this.value === i) {
          className += " active";
        }
        this.$el.append(
          $("<span>", {
            class: className,
            "data-val": i,
          })
        );
      }
      this._renderColorCount();
    },

    _renderReadonly: function () {
      var className = "o_color_pill active readonly o_color_" + this.value;
      this.$el.append(
        $("<span>", {
          class: className,
        })
      );
    },

    clickColorPill: function (ev) {
      var $target = $(ev.currentTarget);
      var data = $target.data();

      this._setValue(data?.val?.toString());
    },
  });

  fieldRegistry.add("int_color", colorField);

  return {
    colorField: colorField,
  };
});
