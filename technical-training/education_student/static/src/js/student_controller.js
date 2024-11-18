odoo.define("student.Controller", function (require) {
  "use strict";

  var AbstractController = require("web.AbstractController");

  var StudentController = AbstractController.extend({
    custom_events: _.extend({}, AbstractController.prototype.custom_events, {
      view_student: "_onClickViewButton",
    }),

    _onClickViewButton: function (ev) {
      this.do_action({
        type: "ir.actions.act_window",
        name: this.title,
        res_model: this.modelName,
        views: [[false, "form"]],
        res_id: ev.data["id"],
      });
    },

    // _onAddButtonClick: function () {
    //   this.do_action({
    //     type: "ir.actions.act_window",
    //     name: this.title,
    //     res_model: this.modelName,
    //     views: [[false, "form"]],
    //     target: "new",
    //   });
    // },
  });

  return StudentController;
});
