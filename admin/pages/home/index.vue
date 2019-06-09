<template>
  <el-row>
    <el-button type="success">Company List</el-button>
    <el-button type="warning">Customer List</el-button>
    <el-button type="danger"><a @click="$router.push({name:'article'})">Article List</a></el-button>
    <el-button type="primary"><a @click="$router.push({name:'news'})">News List</a></el-button>
  </el-row>
</template>
