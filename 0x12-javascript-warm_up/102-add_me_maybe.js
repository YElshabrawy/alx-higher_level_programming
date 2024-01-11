#!/usr/bin/node
function addMeMaybe (n, func) {
  func(++n);
}
module.exports = { addMeMaybe };
