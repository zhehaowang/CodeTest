/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
	var number = 0;
	var visited = new Array(grid.length);
	for (var i = 0; i < grid.length; i++) {
		visited[i] = new Array(grid[i].length);
	}

    for (var i = 0; i < grid.length; i++) {
    	for (var j = 0; j < grid[i].length; j++) {
    		visited[i][j] = 0;
    	}
    }

    // This is not right.
    var checkIsland = function(i, j) {
    	console.log("Checking " + i.toString() + " " + j.toString());
    	if (visited[i][j] !== 0) {
    		return false;
    	} else if (grid[i][j] === '1') {
    		visited[i][j] = 1;
    		if (i + 1 < grid.length) {
    			checkIsland(i + 1, j);
    		} else {

    		}
    		if (j + 1 < grid[0].length) {
    			checkIsland(i, j + 1);
    		} else {

    		}
    		return true;
    	} else {
    		return false;
    	}
    }

    for (var i = 0; i < grid.length; i++) {
    	for (var j = 0; j < grid[i].length; j++) {
    		if (grid[i][j] === '1') {
    			if (checkIsland(i, j) !== false) {
    				console.log("Found island");
    				number += 1;
    			}
    		}
    	}
    }

    return number;
};

var number = numIslands(
	[['1', '0', '1'], 
	 ['0', '1', '1']]);

console.log(number);