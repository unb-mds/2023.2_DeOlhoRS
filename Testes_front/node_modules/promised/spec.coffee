promised = require './index'

describe 'promised', ->

  it 'converts node-style callback API to promise based API', (done) ->
    fs = require 'fs'
    promised(fs).readFile('./README.md')
      .then (content) ->
        done()
      .end()

  it 'patches Object.prototype when needed', (done) ->
    require './patch'
    fs = require 'fs'
    fs.promised.readFile('./README.md')
      .then (content) ->
        done()
      .end()
