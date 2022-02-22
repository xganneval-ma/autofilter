import ResultTable from "./components/ResultTable";
import QueryForm from "./components/QueryForm";

const persons =[{"id":1,"first_name":"Erwan","name":"Arnaud","birthdate":"1968-06-13","gender":{"id":2,"value":"Male"},"email":{"id":1,"type":"email","value":"Erwan.Arnaud@msn.fr","is_public":true,"owner_id":1},"cellphones":[{"id":1,"type":"address","value":"1641384435","is_public":false,"owner_id":1}]},{"id":3,"first_name":"Thibaut","name":"Marechal","birthdate":"1950-03-12","gender":{"id":2,"value":"Male"},"email":{"id":3,"type":"email","value":"Thibaut.Marechal@msn.fr","is_public":true,"owner_id":3},"cellphones":[{"id":2,"type":"address","value":"001-943-738-3881x314","is_public":false,"owner_id":3},{"id":3,"type":"address","value":"048-373-5924","is_public":false,"owner_id":3}]},{"id":4,"first_name":"Lana","name":"Perrier","birthdate":"1980-03-06","gender":{"id":1,"value":"Female"},"email":{"id":4,"type":"email","value":"Lana.Perrier@gmail.com","is_public":false,"owner_id":4},"cellphones":[{"id":4,"type":"address","value":"+1-468-138-3562x0311","is_public":true,"owner_id":4},{"id":5,"type":"address","value":"543-432-1235x692","is_public":true,"owner_id":4}]},{"id":5,"first_name":"Antonin","name":"Leblanc","birthdate":"1945-03-08","gender":{"id":2,"value":"Male"},"email":{"id":5,"type":"email","value":"Antonin.Leblanc@toto.tutu","is_public":true,"owner_id":5},"cellphones":[{"id":6,"type":"address","value":"+1-917-732-7209x61973","is_public":false,"owner_id":5}]},{"id":6,"first_name":"Dominique","name":"Millet","birthdate":"2021-02-27","gender":{"id":2,"value":"Male"},"email":{"id":6,"type":"email","value":"Dominique.Millet@orange.fr","is_public":true,"owner_id":6},"cellphones":[{"id":7,"type":"address","value":"(779)428-0128x1024","is_public":false,"owner_id":6},{"id":8,"type":"address","value":"3744605780","is_public":false,"owner_id":6}]},{"id":7,"first_name":"Hong","name":"Bourgeois","birthdate":"1958-09-01","gender":{"id":3,"value":"Other"},"email":{"id":7,"type":"email","value":"Hong.Bourgeois@msn.fr","is_public":true,"owner_id":7},"cellphones":[{"id":9,"type":"address","value":"6919637724","is_public":true,"owner_id":7},{"id":10,"type":"address","value":"(473)583-9524","is_public":true,"owner_id":7}]}];

function App() {
  return (
    <main className="section">
      <div className="container">
        <h1 className="title">AutoFilter</h1>
        <QueryForm />
        <hr />
        <ResultTable persons={persons}/>
      </div>
    </main>
  );
}

export default App;
