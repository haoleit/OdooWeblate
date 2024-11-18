odoo.define("estate.from_to_date_widget", function (require) {
  "use strict";

  // var AbstractField = require("web.AbstractField");
  var fieldRegistry = require("web.field_registry");
  var FieldDate = require("web.basic_fields").FieldDate;

  var FromToDateWidget = FieldDate.extend({
    supportedFieldTypes: ["date"],

    // events: {
    //   "click .date-picker-button": "_onOpenDatePicker",
    // },

    _renderReadonly: function () {
      this.$el.empty();
      var formattedFromDate = this._formatDateMMYYYY(
        this.record.data.from_date
      );
      var formattedToDate = this._formatDateMMYYYY(this.record.data.to_date);
      var displayText =
        (formattedFromDate || "From Date") +
        " - " +
        (formattedToDate || "To Date");
      this.$el.text(displayText);
    },

    _renderEdit: function () {
      this.$el.empty();
      var $input = $("<input>")
        .attr("type", "text")
        .addClass("from-to-date-picker")
        .attr("placeholder", "From Date - To Date");
      this.$el.append($input);

      this._initializeDateRangePicker($input);
    },

    _initializeDateRangePicker: function ($input) {
      var self = this;
      $(".bootstrap-datetimepicker-widget").remove();
      $input.daterangepicker(
        {
          opens: "right",
          alwaysShowCalendars: true,
          autoUpdateInput: false,
          startDate: this.record.data.from_date
            ? moment(this.record.data.from_date)
            : moment(),
          endDate: this.record.data.to_date
            ? moment(this.record.data.to_date)
            : moment(),
          locale: {
            format: "MM/DD/YYYY",
            separator: " - ",
            applyLabel: "Apply",
            cancelLabel: "Clear",
            customRangeLabel: "Custom Range",
          },
          ranges: {
            Today: [moment(), moment()],
            Yesterday: [
              moment().subtract(1, "days"),
              moment().subtract(1, "days"),
            ],
            "Last 7 Days": [moment().subtract(6, "days"), moment()],
            "Last 30 Days": [moment().subtract(29, "days"), moment()],
            "This Month": [moment().startOf("month"), moment().endOf("month")],
            "Last Month": [
              moment().subtract(1, "month").startOf("month"),
              moment().subtract(1, "month").endOf("month"),
            ],
          },
        },
        function (start, end) {
          // Save selected dates\
          $input.val(
            start.format("MM/DD/YYYY") + " - " + end.format("MM/DD/YYYY")
          );
          self._setValue({
            from_date: start.format("YYYY-MM-DD"),
            to_date: end.format("YYYY-MM-DD"),
          });
        }
      );

      // Handle "Apply" button to ensure no overlapping calendars
      $input.on("apply.daterangepicker", function () {
        $input.data("daterangepicker").hide(); // Hide calendar after apply
        $(".bootstrap-datetimepicker-widget").remove();
      });
    },

    /**
     * Format the date as MM/YYYY
     */
    _formatDateMMYYYY: function (date) {
      if (!date) {
        return "";
      }
      var dateObj = moment(date);
      return dateObj.format("MM/YYYY");
    },

    /**
     * Set the value for the widget
     */
    _setValue: function (dates) {
      this.trigger_up("field_changed", {
        dataPointID: this.dataPointID,
        changes: { from_date: dates.from_date, to_date: dates.to_date },
        fieldName: this.name,
      });
    },
  });

  fieldRegistry.add("from_to_date_custom", FromToDateWidget);

  return FromToDateWidget;
});
