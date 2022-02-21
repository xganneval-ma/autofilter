const Lt = (field: OperatorLt['field'], value: OperatorLt['value']): OperatorLt => {
    return {
      type: "Lt",
      field,
      value,
    };
  };
  
  export default Lt;
  