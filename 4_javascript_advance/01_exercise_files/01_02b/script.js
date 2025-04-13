const data = [
  { id: 1, parent: 0, text: 'Top-level comment 1' },
  { id: 2, parent: 0, text: 'Top-level comment 2' },
  { id: 3, parent: 1, text: 'Reply to top-level comment 1' },
  { id: 4, parent: 3, text: 'Reply to reply to top-level comment 1' },
];

/**
 * Restructure the flat data array into a nested array
 * 
 * @param {array} data
 * @returns {array} 
*/

function restructureArray(data) {
  const dataMap = {};

  // Create and array to hold the root elements
  const root = [];

  data.forEach((item) => {
    dataMap[item.id] = {
      ...item,
      children: [],
    };
  });

  return root;
}

const result = restructureArray(data);

// Output the result array as a tree

console.log(JSON.stringify(result, null, 2));