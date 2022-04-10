import logo from './logo.png';
import './App.css';
import Search from './components/Search'

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <br/><br/>
        <p>
          CS411: Flight Cancellation
        </p>
        <Search/>
        <a
          className="Repo-Link"
          href="https://github.com/rithvik-doshi/CS411-Project-Team4"
          target="_blank"
          rel="noopener noreferrer"
        >
          Link to GitHub
        </a>
      </header>
    </div>
  );
}

export default App;
