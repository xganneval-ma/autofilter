const Lte = (field: OperatorLte['field'], value: OperatorLte['value']): OperatorLte => {
    return {
      type: "Lte",
      field,
      value,
    };
  };
  
  export default Lte;
  