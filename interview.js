const remove_dulplicate = (string) => {
  const uniChars = new Set();
  for(let i=0; i < string.length; i++) {
    char = string.charAt(i);
    if (! uniChars.has(char)) {
      uniChars.add(char)
    }
  }
  let result = '';
  uniChars.forEach((char) =>{
    result = result.concat(char);
  });
  return result

};
console.log(remove_dulplicate('hello world'));
