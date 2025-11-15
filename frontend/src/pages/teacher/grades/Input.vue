<script lang="ts">
export const description = "Teacher grade input page"
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
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbLink,
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
import { Input } from "@/components/ui/input"
import { Select, SelectTrigger, SelectItem, SelectContent, SelectValue } from "@/components/ui/select"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import { Save, Pencil, Users } from "lucide-vue-next"

const userRole = "Teacher"

// Mock class & student data
const subjectInfo = ref({
  subject: "General Mathematics",
  section: "STEM 11 - A",
  teacher: "Maria Santos",
})

const quarter = ref("1st Quarter")

const students = ref([
  { id: 1, name: "Carlos Dela Cruz", grade: 89 },
  { id: 2, name: "Maria Santos", grade: 92 },
  { id: 3, name: "John Perez", grade: 85 },
  { id: 4, name: "Angela Ramos", grade: 94 },
  { id: 5, name: "Mark Rivera", grade: 88 },
])
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
              <BreadcrumbPage>Grade Input</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col p-4 pt-0 gap-4">

        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Grade Input</h2>
            <p class="text-sm text-muted-foreground">
              Input and update student grades for this subject.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Save class="h-4 w-4" />
            Save Grades
          </Button>
        </div>

        <!-- Subject Info -->
        <Card>
          <CardHeader>
            <CardTitle>Class Details</CardTitle>
            <CardDescription>Review and verify the subject and section information.</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid gap-4 md:grid-cols-3">
              <div>
                <p class="text-sm text-muted-foreground">Subject</p>
                <p class="font-semibold">{{ subjectInfo.subject }}</p>
              </div>
              <div>
                <p class="text-sm text-muted-foreground">Section</p>
                <p class="font-semibold">{{ subjectInfo.section }}</p>
              </div>
              <div>
                <p class="text-sm text-muted-foreground">Teacher</p>
                <p class="font-semibold">{{ subjectInfo.teacher }}</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Quarter Selector -->
        <div class="flex items-center gap-4">
          <p class="font-medium">Select Quarter:</p>

          <Select v-model="quarter">
            <SelectTrigger class="w-48">
              <SelectValue placeholder="Select Quarter" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="1st Quarter">1st Quarter</SelectItem>
              <SelectItem value="2nd Quarter">2nd Quarter</SelectItem>
              <SelectItem value="3rd Quarter">3rd Quarter</SelectItem>
              <SelectItem value="4th Quarter">4th Quarter</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <!-- Grade Table -->
        <Card>
          <CardHeader>
            <CardTitle>Students</CardTitle>
            <CardDescription>Enter grades for each student below.</CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead class="w-32">Grade</TableHead>
                  <TableHead class="text-right w-20">Action</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="student in students"
                  :key="student.id"
                  class="hover:bg-muted/50"
                >
                  <TableCell class="font-medium">
                    <div class="flex items-center gap-2">
                      <Users class="h-4 w-4 text-muted-foreground" />
                      {{ student.name }}
                    </div>
                  </TableCell>

                  <TableCell>
                    <Input
                      v-model="student.grade"
                      class="w-24"
                      type="number"
                      min="0"
                      max="100"
                    />
                  </TableCell>

                  <TableCell class="text-right">
                    <Button variant="ghost" size="icon">
                      <Pencil class="h-4 w-4" />
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
