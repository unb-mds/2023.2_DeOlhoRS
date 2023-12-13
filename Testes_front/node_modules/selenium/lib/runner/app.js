var util  = require('util'),
    spawn = require('child_process').spawn,
    fs    = require('fs'),
    wd    = __dirname + '/../..',
    selenium    
          = spawn(
              'java', 
              ['-jar', __dirname + '/selenium-server-standalone-2.20.0.jar']
            ),
    ok    = false,
    out   = fs.createWriteStream(wd + '/logs/selenium.out', {flags: 'a'}),
    err   = fs.createWriteStream(wd + '/logs/selenium.err', {flags: 'a'});

selenium.stderr.on('data', function(data) {
  if (/^execvp\(\)/.test(data)) {
    console.log('Failed to start selenium. Please ensure that java '+
      'is in your system path');
  }
  else if (!ok) {
    ok = true;
    console.log("Selenium is started.");
    console.log("All output can be found at: " + wd + '/logs');
  }
})

util.pump(selenium.stdout, out);
util.pump(selenium.stderr, err);
