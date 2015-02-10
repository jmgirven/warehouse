module.exports = function (grunt) {
    grunt.initConfig({

    // define source files and their destinations
    uglify: {
        files: { 
            src: 'js/app/**/*.js',  // source files mask
            dest: 'js/jsm/',    // destination folder
            expand: true,    // allow dynamic building
            flatten: true,   // remove all unnecessary nesting
            ext: '.min.js'   // replace .js to .min.js
        }
    },
    cssmin: {
    	files: { 
    		cwd: 'css/',
            src: ['*.css', '!*.min.css'],  // source files mask
            dest: 'css/',    // destination folder
            expand: true,    // allow dynamic building
            ext: '.min.css'   // replace .css to .min.css
        }
    }, 
    watch: {
        js:  { files: 'js/app/**/*.js', tasks: [ 'uglify' ] },
        css:  { files: ['css/*.css', 'css/!*.min.css'], tasks: [ 'cssmin' ] }
    }
});

// load plugins
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-cssmin');

// register tasks
grunt.registerTask('default', [ 'uglify', 'cssmin' ]);

};
