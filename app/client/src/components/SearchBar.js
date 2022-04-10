import React from 'react';
const SearchBar = ({keyword, setKeyword}) => {

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      setKeyword(event.target.value)
    }
  }

  const BarStyling = {width:"24rem",background:"#F2F1F9", border:"none", padding:"0.5rem"};

  return (
    <>
    <input
    style={BarStyling}
     key="random1"
     value={keyword}
     class="form-control"
     placeholder={"Enter flight number, e.g. AS139"}
    //  onChange={(e) => setKeyword(e.target.value)}
     onKeyDown={(e) => handleKeyDown(e)}
    />
    </>
  );
}
export default SearchBar