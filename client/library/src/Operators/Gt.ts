const Gt = (field: OperatorGt['field'], value: OperatorGt['value']): OperatorGt => {
    return {
      type: "Gt",
      field,
      value,
    };
  };
  
  export default Gt;
  