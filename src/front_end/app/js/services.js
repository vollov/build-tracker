'use strict';

buildApp.factory('Build', function($resource) {
	return $resource('/api/builds/:id', {id: '@id'}, {
        update: {method:'PUT'}
    });
});
