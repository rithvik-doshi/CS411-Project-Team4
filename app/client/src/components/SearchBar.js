import React, {useState} from 'react';
const SearchBar = ({keyword, dateKeyword, setKeyword}) => {

  const [date, setDate] = useState();

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      console.log(event.target.value, date)
      setKeyword(event.target.value, date)
    }
  }

  const BarStyling = {width:"24rem",background:"#F2F1F9", border:"none", padding:"0.5rem"};

  return (
    <>
    <input
    style={BarStyling}
     key="random2"
     value={dateKeyword}
     class="form-control"
     placeholder={"Enter flight date: YYYY-MM-DD"}
     onChange={(e) => setDate(e.target.value)}
    />
    <br/>
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