const And = (...oprsOrExprs: ExpressionLink['children']): ExpressionLink => {
  return {
    type: "And",
    children: oprsOrExprs,
  };
};

export default And;
