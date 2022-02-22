import ResultTable from "./components/ResultTable";
import { useState } from "react";
import QueryForm from "./components/QueryForm";

function App() {
  const [data, setData] = useState(null);
  console.log(data)

  return (
    <main className="section">
      <div className="container">
        <h1 className="title">AutoFilter</h1>
        <QueryForm updateData={setData} />
        <hr />
        <ResultTable persons={data}/>
      </div>
    </main>
  );
}

export default App;
