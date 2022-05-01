import React, { useCallback, useEffect, useState } from 'react';
import SearchBar from './SearchBar';

const parseString = (string) => {
    const data = JSON.parse(string);
    console.log(data.ident) // TO REMOVE
    string = data.ident
    return string + ", left on " + data.actual_off + " from " + data.origin.code_iata +
     " and arrived on " + data.actual_on + " at " + data.destination.code_iata;
}

export default function Search({clearResults}) {
    const [input, setInput] = useState('');
    const [date, setDate] = useState();
    const [data, setData] = useState();
    const [isErrorMsgVisible, setIsErrorMsgVisible] = useState(false);

    const clearOutput = useCallback(() => {
        setData(null);
    }, []);

    useEffect(() => {
        clearOutput();
    }, [clearResults, clearOutput]);

    // const isValidEmailAddress = (email) => {
    //     return /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
    // };

    const updateSearch = async (input, date) => {
        clearOutput();
        setInput(input);
        setDate(date);

        if (input === "" || date === "") {
            setIsErrorMsgVisible(false);
            return null;
        }

        const URL = 'http://127.0.0.1:5000/search/';
        //console.log(`${URL}${input}/${date}`)

        await Promise.allSettled([ 
                // DUO
            fetch(`${URL}${input}/${date}`)
            .then(response => response.json())
            .then(data => {
                console.log(data); // TO REMOVE
                if (data) {
                    setData(parseString(JSON.stringify(data)));
                }
            })
        ])
    }

    return (
        <div id="search" align="center">
            <SearchBar
              input={input}
              date={date}
              setKeyword={updateSearch}
            />
            { isErrorMsgVisible && (
                <div className="error">Error.</div>
            )}
            <p>{data}</p>
        </div>
    );
}