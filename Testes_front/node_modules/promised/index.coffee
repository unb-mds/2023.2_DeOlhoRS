{defer} = require 'kew'

promisifyFunction = (func, bind = null) ->
  return func.__promisified__ if func.__promisified__
  func.__promisified__ = (args...) ->
    promise = defer()
    func.call bind, args..., (err, result) =>
      if err
        promise.reject(err)
      else
        promise.resolve(result)
    promise
  func.__promisified__

promisifyObject = (obj) ->
  return obj.__promisified__ if obj.__promisified__
  nObj = Object.create(obj)
  for k, v of obj when typeof v == 'function'
    nObj[k] = promisifyFunction(v, obj)
  obj.__promisified__ = nObj
  obj.__promisified__

module.exports = (o, bind) ->
  if typeof o == 'function'
    promisifyFunction(o, bind)
  else
    promisifyObject(o)

module.exports.promiseToCallback = (promise, cb) ->
  promise
    .then (result) ->
      cb(null, result)
    .fail (err) ->
      cb(err)
  undefined
