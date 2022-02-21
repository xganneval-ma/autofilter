const Not = (operator: ExpressionNot["operator"]): ExpressionNot => {
  return {
    type: "Not",
    operator,
  };
};

export default Not;
