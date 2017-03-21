angular.module('colin.search')
    .controller('ColinSearchController', ['SearchTerm', '$scope', function(SearchTerm, $scope) {
        var vm = this;
        console.log("tevin campbell");
        vm.searching = false;

        $scope.$on("searchTerm:changed", function(event, data) {
              vm.searching = SearchTerm.get() !== "";
              console.log(vm.searching);
          });


    }]);