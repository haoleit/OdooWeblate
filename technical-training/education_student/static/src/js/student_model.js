odoo.define("student.Model", function (require) {
  "use strict";

  var AbstractModel = require("web.AbstractModel");

  var StudentModel = AbstractModel.extend({
    init: function () {
      this._super.apply(this, arguments);
      this.data = null;
    },
    get: function () {
      return this.data;
    },
    __load: function (params) {
      this.modelName = params.modelName;
      this.context = params.context;
      this.domain = params.domain;
      return this._fetchData();
    },
    __reload: function (handle, params) {
      if ("domain" in params) this.domain = params.domain;
      return this._fetchData();
    },
    _fetchData: function () {
      var self = this;
      return this._rpc({
        model: this.modelName,
        method: "search_read",
        context: this.context,
        domain: this.domain,
      }).then(function (results) {
        self.data = results.map((result) => ({
          id: result.id,
          display_name: result.display_name,
          image: result.image_1024,
        }));
      });
    },
  });

  return StudentModel;
});
