odoo.define("estate.mm_yyyy_widget", function (require) {
  "use strict";

  var AbstractField = require("web.AbstractField");
  var fieldRegistry = require("web.field_registry");
  var field_utils = require("web.field_utils");
  var FieldDate = require("web.basic_fields").FieldDate;

  var DateMMYYYYWidget = FieldDate.extend({
    supportedFieldTypes: ["date"],

    _formatDateMMYYYY: function (date) {
      if (!date) {
        return "";
      }
      var dateObj = field_utils.parse.date(date);
      return moment(dateObj).format("MM/YYYY");
    },

    _renderReadonly: function () {
      this.$el.empty();
      var formattedDate = this._formatDateMMYYYY(this.value);
      this.$el.text(formattedDate || "MM/YYYY");
    },

    _renderEdit: function () {
      // Use the default FieldDate behavior for edit mode
      this._super.apply(this, arguments);
    },
  });

  fieldRegistry.add("mm_yyyy", DateMMYYYYWidget);

  return DateMMYYYYWidget;
});
