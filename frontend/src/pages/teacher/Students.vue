<script lang="ts">
export const description = "Teacher students list"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"

import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHead,
  TableHeader,
  TableRow,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  Users,
  GraduationCap,
  UserCheck,
  Search,
  Eye,
} from "lucide-vue-next"

const userRole = "Teacher"

// Mock students data
const students = ref([
  { id: 1, name: "Carlos Dela Cruz", gender: "Male", grade: "Grade 11", section: "STEM A", status: "Active" },
  { id: 2, name: "Maria Santos", gender: "Female", grade: "Grade 11", section: "STEM A", status: "Active" },
  { id: 3, name: "John Perez", gender: "Male", grade: "Grade 11", section: "STEM A", status: "Inactive" },
  { id: 4, name: "Angela Ramos", gender: "Female", grade: "Grade 11", section: "STEM A", status: "Active" },
  { id: 5, name: "Mark Rivera", gender: "Male", grade: "Grade 11", section: "STEM A", status: "Active" },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Students</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Page Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Students</h2>
            <p class="text-sm text-muted-foreground">View and manage your students.</p>
          </div>

          <Button variant="outline">
            <Search class="mr-2 h-4 w-4" />
            Search
          </Button>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-3">
          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Total Students</CardTitle>
              <Users class="h-5 w-5 text-primary" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">{{ students.length }}</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Active Students</CardTitle>
              <UserCheck class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ students.filter(s => s.status === 'Active').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Grade Level</CardTitle>
              <GraduationCap class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">Grade 11</p>
            </CardContent>
          </Card>
        </div>

        <!-- Students Table -->
        <Card>
          <CardHeader>
            <CardTitle>Student List</CardTitle>
            <CardDescription>
              List of all students under your classes.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <div class="flex items-center justify-between mb-4">
              <Input v-model="search" placeholder="Search students..." class="max-w-xs" />
            </div>

            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student Name</TableHead>
                  <TableHead>Gender</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="student in students"
                  :key="student.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell class="font-medium">
                    {{ student.name }}
                  </TableCell>

                  <TableCell class="text-muted-foreground">{{ student.gender }}</TableCell>

                  <TableCell>{{ student.grade }}</TableCell>

                  <TableCell>{{ student.section }}</TableCell>

                  <TableCell>
                    <Badge
                      :variant="student.status === 'Active' ? 'default' : 'secondary'"
                    >
                      {{ student.status }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-right">
                    <Button variant="outline" size="sm">
                      <Eye class="h-4 w-4 mr-1" />
                      View
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
