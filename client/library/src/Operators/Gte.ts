const Gte = (field: OperatorGte['field'], value: OperatorGte['value']): OperatorGte => {
    return {
      type: "Gte",
      field,
      value,
    };
  };
  
  export default Gte;
  