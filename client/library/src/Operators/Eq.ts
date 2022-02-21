const Eq = (field: OperatorEq['field'], value: OperatorEq['value']): OperatorEq => {
  return {
    type: "Eq",
    field,
    value,
  };
};

export default Eq;
