odoo.define("student.View", function (require) {
  "use strict";

  var AbstractView = require("web.AbstractView");
  var view_registry = require("web.view_registry");
  var StudentController = require("student.Controller");
  var StudentModel = require("student.Model");
  var StudentRenderer = require("student.Renderer");

  var StudentView = AbstractView.extend({
    display_name: "Student",
    icon: "fa-id-card-o",
    config: _.extend({}, AbstractView.prototype.config, {
      Model: StudentModel,
      Controller: StudentController,
      Renderer: StudentRenderer,
    }),
    viewType: "student",
    searchMenuTypes: ["filter", "favorite"],
  });

  view_registry.add("student", StudentView);
  return StudentView;
});
