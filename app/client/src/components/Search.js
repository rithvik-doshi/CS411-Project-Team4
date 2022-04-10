import React, { useCallback, useEffect, useState } from 'react';
import SearchBar from './SearchBar';

export default function Search({clearResults}) {
    const [input, setInput] = useState('');
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

    const updateSearch = async (input) => {
        clearOutput();
        setInput(input);

        if (input === "") {
            setIsErrorMsgVisible(false);
            return null;
        }

        const URL = 'http://127.0.0.1:5000/search/';

        await Promise.allSettled([ 
                // DUO
            fetch(`${URL}${input}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data) {
                    setData(JSON.stringify(data));
                }
            })
        ])
    }

    return (
        <div id="search">
            <SearchBar
              input={input}
              setKeyword={updateSearch}
            />
            { isErrorMsgVisible && (
                <div className="error">Error.</div>
            )}
            <p>{data}</p>
        </div>
    );
}