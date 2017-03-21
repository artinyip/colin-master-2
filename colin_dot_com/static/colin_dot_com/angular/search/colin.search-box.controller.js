angular.module('colin.search').
    controller('colin.search-box', ['SearchTerm',
        function(SearchTerm) {
            var ctrl = this;
            ctrl.term = "";
            this.search = function () {
                SearchTerm.set(ctrl.term);
            }
        }
    ]);