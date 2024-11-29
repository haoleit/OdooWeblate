odoo.define("estate.TreeViewCheckboxExtend", function (require) {
  "use strict";

  const CheckboxWidgetController =
    require("estate.TreeViewButton").TreeViewButtonDemoWidgetController;
  const ListRenderer = require("web.ListRenderer");
  const viewRegistry = require("web.view_registry");
  const ListView = require("web.ListView");
  const core = require("web.core");

  const qweb = core.qweb;

  // Extend ListController to handle events
  const ExtendedTreeViewCheckboxController = CheckboxWidgetController.extend({
    renderButtons: function ($node) {
      this._super.apply(this, arguments);

      const hideColorChecked = JSON.parse(
        localStorage.getItem("hideColor") || "false"
      );

      const hideDateChecked = JSON.parse(
        localStorage.getItem("hideDate") || "false"
      );

      if (this.$buttons) {
        // Render buttons using QWeb template
        const $template = $(qweb.render("TreeView.Checkboxes"));
        this.$buttons.append($template);

        // Apply stored states to checkboxes
        this.$buttons
          .find(".hide-color-checkbox")
          .prop("checked", hideColorChecked);

        this.$buttons
          .find(".hide-color-checkbox")
          .prop("disabled", hideColorChecked);

        this.$buttons
          .find(".hide-date-checkbox")
          .prop("checked", hideDateChecked);

        this.$buttons
          .find(".hide-date-checkbox")
          .prop("disabled", hideDateChecked);

        // Show or hide Apply and Clear buttons based on stored states
        this.$buttons
          .find(".apply-button")
          .toggle(hideColorChecked || hideDateChecked);
        this.$buttons
          .find(".clear-button")
          .toggle(hideColorChecked || hideDateChecked);

        // Attach event listeners
        this.$buttons
          .find(".hide-color-checkbox, .hide-date-checkbox")
          .on("change", this._onCheckboxChange.bind(this));
        this.$buttons
          .find(".apply-button")
          .on("click", this._onApplyButtonClick.bind(this));
        this.$buttons
          .find(".clear-button")
          .on("click", this._onClearButtonClick.bind(this));
      }
    },

    _onCheckboxChange: function () {
      const hideColorChecked = this.$buttons
        .find(".hide-color-checkbox")
        .is(":checked");
      const hideDateChecked = this.$buttons
        .find(".hide-date-checkbox")
        .is(":checked");

      // Show Apply button if at least one checkbox is checked
      this.$buttons
        .find(".apply-button")
        .toggle(hideColorChecked || hideDateChecked);

      // Show Clear button if any field is hidden
      this.$buttons
        .find(".clear-button")
        .toggle(hideColorChecked || hideDateChecked);
    },

    _onApplyButtonClick: function () {
      let context = this.model.get(this.handle, { raw: true }).getContext();
      const hideColorChecked = this.$buttons
        .find(".hide-color-checkbox")
        .is(":checked");
      const hideDateChecked = this.$buttons
        .find(".hide-date-checkbox")
        .is(":checked");

      // Call renderer to toggle field visibility
      // this.renderer.toggleFields({
      //   hideColor: hideColorChecked,
      //   hideDate: hideDateChecked,
      // });

      context = {
        ...context,
        hideColor: hideColorChecked,
        hideDate: hideDateChecked,
      };

      // Save states to local storage
      localStorage.setItem("hideColor", JSON.stringify(hideColorChecked));
      localStorage.setItem("hideDate", JSON.stringify(hideDateChecked));

      this.trigger_up("do_action", {
        action: {
          type: "ir.actions.act_window",
          res_model: "demo.widget",
          name: "Demo Widget",
          context: context,
          views: [[false, "list"]],
          target: "current",
        },
        options: {
          clear_breadcrumbs: true,
        },
      });
    },

    _onClearButtonClick: function () {
      // Reset all checkboxes
      let context = this.model.get(this.handle, { raw: true }).getContext();
      this.$buttons
        .find(".hide-color-checkbox, .hide-date-checkbox")
        .prop("checked", false);

      // Reset field visibility
      // this.renderer.toggleFields({ hideColor: false, hideDate: false });

      context = {
        ...context,
        hideColor: false,
        hideDate: false,
      };

      // Save reset states to local storage
      localStorage.setItem("hideColor", JSON.stringify(false));
      localStorage.setItem("hideDate", JSON.stringify(false));

      this.trigger_up("do_action", {
        action: {
          type: "ir.actions.act_window",
          res_model: "demo.widget",
          name: "Estate Widget",
          context: context,
          views: [[false, "list"]],
          target: "current",
        },
        options: {
          clear_breadcrumbs: true,
        },
      });

      // Hide Apply and Clear buttons
      this.$buttons.find(".apply-button, .clear-button").hide();
    },
  });

  // Extend ListRenderer for managing field visibility
  const ExtendedTreeViewCheckboxRenderer = ListRenderer.extend({
    toggleFields: function (options) {
      const { hideColor, hideDate } = options;

      this.columnInvisibleFields["color"] = hideColor;
      $(".hide-color-checkbox").prop("disabled", hideColor);
      this.columnInvisibleFields["from_date"] = hideDate;
      this.columnInvisibleFields["to_date"] = hideDate;
      $(".hide-date-checkbox").prop("disabled", hideDate);
      this._processColumns(this.columnInvisibleFields);

      // Re-render the list view to apply changes
      this._renderView();
    },
  });

  // Extend ListView to integrate logic
  const ExtendedTreeViewCheckboxListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
      Controller: ExtendedTreeViewCheckboxController,
      Renderer: ExtendedTreeViewCheckboxRenderer,
    }),
  });

  // Register the new view
  viewRegistry.add(
    "tree_with_button_and_checkbox",
    ExtendedTreeViewCheckboxListView
  );

  return {
    ExtendedTreeViewCheckboxController: ExtendedTreeViewCheckboxController,
    ExtendedTreeViewCheckboxRenderer: ExtendedTreeViewCheckboxRenderer,
  };
});
