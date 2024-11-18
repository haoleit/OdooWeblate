odoo.define("estate.TreeViewButton", function (require) {
  "use strict";

  const ListRenderer = require("web.ListRenderer");
  const ListController = require("web.ListController");
  const viewRegistry = require("web.view_registry");

  const ListView = require("web.ListView");

  // Extend the ListRenderer to add a custom button only for demo.widget model
  // const TreeViewButtonRenderer = ListRenderer.extend({
  //   renderButtons: function ($node) {
  //     if (this.state.model !== "demo.widget") {
  //       return this._super.apply(this, arguments);
  //     }

  //     this._super.apply(this, arguments);

  //     // Create the custom button
  //     const $button = $("<button>", {
  //       type: "button",
  //       class: "btn btn-primary",
  //       text: "Click Me",
  //     }).on("click", this._onButtonClick.bind(this));

  //     // Append the button to the header
  //     this.buttons.append($button);
  //   },

  //   _onButtonClick: function () {
  //     this.do_notify("Button Clicked", "You clicked the button in the header!");
  //   },
  // });

  const TreeViewButtonDemoWidgetController = ListController.extend({
    renderButtons: function ($node) {
      this._super.apply(this, arguments);

      if (this.$buttons) {
        const $button = $("<button>", {
          type: "button",
          class: "btn btn-primary",
          text: "Click Me",
        }).on("click", this._onButtonClick.bind(this));

        this.$buttons.prepend($button);
      }
    },

    _onButtonClick: function () {
      this.do_notify(
        "'Inventory Overview' added to dashboard",
        "Please refresh your browser for the changes to take effect."
      );
    },
  });

  // Override ListView to use the custom renderer and controller for demo.widget only
  const TreeViewButtonListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
      // Renderer: TreeViewButtonRenderer,
      Controller: TreeViewButtonDemoWidgetController,
    }),
  });

  // Register the view only for demo.widget model
  viewRegistry.add("tree_with_button", TreeViewButtonListView);

  return {
    TreeViewButtonDemoWidgetController: TreeViewButtonDemoWidgetController,
  };
});
