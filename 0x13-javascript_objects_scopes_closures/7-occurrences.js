#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  list.forEach(itm => {
    if (itm === searchElement) c++;
  });
  return c;
};
