import { useState } from "react";
import axios from "axios";

// import Query, { Eq } from "@ma-hackathon/auto-filter";

// eslint-disable-next-line react/prop-types
function QueryForm({ updateData }) {
  const [currentChecked, setCurrentChecked] = useState("");

  const clickHandler = (queryType) => {
    setCurrentChecked(queryType);
    let query = "";

    switch (queryType) {
      case "firstNameQuery":
        query = `Eq(first_name, 'Erwan')`;
        break;
      case "emailQuery":
        query = `Like(email.value, '%maelle%')`;
        break;
      case "betweenDate":
        query = `Btw(birthdate, '1990-02-21', '1995-02-21')`;
        break;
      case "orBetweenDate":
        query = `Or(Btw(birthdate, '1990-02-21', '1995-02-21'), Btw(birthdate, '2000-02-21', '2005-02-21'))`;
        break;
      default:
        query = "";
    }

    axios
      .get("/api/person/", { params: { q: query } })
      .then((res) => {
        updateData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <section>
      <h2 id="form-title">Query</h2>
      <form aria-labelledby="form-title" onSubmit={(e) => e.preventDefault()}>
        <div>
          <input
            type="checkbox"
            id="checkbox1"
            className="mr-2"
            checked={currentChecked === "allPeople"}
            onClick={() => clickHandler("allPeople")}
          />
          <label className="checkbox" htmlFor="checkbox1">
            All people
          </label>
        </div>
        <div>
          <input
            type="checkbox"
            id="checkbox2"
            className="mr-2"
            checked={currentChecked === "firstNameQuery"}
            onClick={() => clickHandler("firstNameQuery")}
          />
          <label className="checkbox" htmlFor="checkbox2">
            People named Erwan
          </label>
        </div>
        <div>
          <input
            type="checkbox"
            id="checkbox3"
            className="mr-2"
            checked={currentChecked === "emailQuery"}
            onClick={() => clickHandler("emailQuery")}
          />
          <label className="checkbox" htmlFor="checkbox3">
            Email containing maelle
          </label>
        </div>
        <div>
          <input
            type="checkbox"
            id="checkbox4"
            className="mr-2"
            onClick={() => clickHandler("betweenDate")}
            checked={currentChecked === "betweenDate"}
          />
          <label className="checkbox" htmlFor="checkbox4">
            Birthdate between 1990-02-21 and 1995-02-21
          </label>
        </div>
        <div>
          <input
            type="checkbox"
            id="checkbox5"
            className="mr-2"
            checked={currentChecked === "orBetweenDate"}
            onClick={() => clickHandler("orBetweenDate")}
          />
          <label className="checkbox" htmlFor="checkbox5">
            Birthdate between 1990-02-21 and 1995-02-21 OR between 2000-02-21
            and 2005-02-21
          </label>
        </div>
      </form>
    </section>
  );
}

export default QueryForm;
