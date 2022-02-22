function QueryForm() {
  return (
    <section>
      <h2 id="form-title">Query</h2>
      <form aria-labelledby="form-title" onSubmit={(e) => e.preventDefault()}>
        <div>
          <input type="checkbox" id="checkbox1" className="mr-2" />
          <label className="checkbox" htmlFor="checkbox1">
            Checkbox 1
          </label>
        </div>
        <div>
          <input type="checkbox" id="checkbox2" className="mr-2" />
          <label className="checkbox" htmlFor="checkbox2">
            Checkbox 2
          </label>
        </div>
        <div>
          <input type="checkbox" id="checkbox3" className="mr-2" />
          <label className="checkbox" htmlFor="checkbox3">
            Checkbox 3
          </label>
        </div>
      </form>
    </section>
  );
}

export default QueryForm;
